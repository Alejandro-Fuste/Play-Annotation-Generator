# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_17`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_17/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [66–78], lower_priority='Action_RunBlock' annotated_start=70, effective_Action_RunBlock_start=79.
> - Action 'Action_None' range [66-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [70-209] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-263] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-156] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [70-269] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [70-132] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-223] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-100] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-266] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [66-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [79-85] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [92-93] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [111-114] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [117-123] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [126-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [132-142] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [152-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [156-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [70-155] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '27' has 1 frames without a visible bounding box.
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