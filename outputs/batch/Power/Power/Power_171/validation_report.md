# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_171`
- **Input XML**: `outputs/batch/Power/Power/Power_171/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 344: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PullBlock' range [107-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [107-116] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-167] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-139] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-153] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-240] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-267] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-224] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-190] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-274] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-294] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-298] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-176] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-201] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-283] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-181] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-195] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-151] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-257] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-273] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-14] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-45] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-299] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-9] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-14] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-141] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-144] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-299] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-195] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-200] for track '30' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.