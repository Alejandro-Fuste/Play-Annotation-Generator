# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_341`
- **Input XML**: `outputs/batch/Power/Power/Power_341/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 12 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 682: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - Row 682: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 682: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-193] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-132] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-221] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-162] for track '14' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-196] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [110-115] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [119-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [127-143] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-114] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [105-144] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-137] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '27' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
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