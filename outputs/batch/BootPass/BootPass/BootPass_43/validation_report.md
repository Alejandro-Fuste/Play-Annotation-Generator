# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_43`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_43/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 63 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [34–48], lower_priority='Action_RunBlock' annotated_start=42, effective_Action_RunBlock_start=49.
> - Action 'Action_None' range [204-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-106] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-134] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-205] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-187] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [34-48] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [49-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [75-146] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [149-203] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [42-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '25' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.