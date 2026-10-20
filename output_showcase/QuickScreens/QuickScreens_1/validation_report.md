# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `QuickScreens_1`
- **Input XML**: `output_showcase/QuickScreens/QuickScreens_1/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/QuickScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 62 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [22-164] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-52] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-196] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-63] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [99-197] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [201-210] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-153] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-113] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-148] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-166] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '23' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.