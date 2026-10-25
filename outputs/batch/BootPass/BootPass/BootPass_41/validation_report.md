# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_41`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_41/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [25–41], lower_priority='Action_RunBlock' annotated_start=36, effective_Action_RunBlock_start=42.
> - Action 'Action_None' range [25-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SecureCatch' range [204-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-187] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-63] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-71] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [36-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-88] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [36-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-171] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [36-75] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [81-210] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [36-41] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-85] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-102] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-156] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '29' has 1 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.