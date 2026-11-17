# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_127`
- **Input XML**: `outputs/batch/Power/Power/Power_127/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 65 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_PreSnap' range [0-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-280] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-190] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-272] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-276] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-298] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-277] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-284] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-203] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-212] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-218] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-265] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-135] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-188] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-50] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-192] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-208] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-157] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-210] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-25] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [125-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [132-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-214] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-276] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-214] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-287] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-254] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-258] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [294-299] for track '27' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.