# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_15`
- **Input XML**: `outputs/batch/Power/Power/Power_15/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 32: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-113] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-177] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-210] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-151] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-193] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-103] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [61-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-145] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [61-73] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [76-118] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-208] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [61-118] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-67] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-112] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-205] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-187] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-204] for track '27' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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