# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SlantAndGo_47`
- **Input XML**: `outputs/batch/SlantAndGo/SlantAndGo/SlantAndGo_47/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SlantAndGo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [10–27], lower_priority='Action_PassBlock' annotated_start=20, effective_Action_PassBlock_start=28.
> - Action 'Action_None' range [10-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-170] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-176] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-71] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_VerticalStem' range [87-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-94] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-105] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-140] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-152] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-31] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [35-132] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [28-126] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-45] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-12] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-19] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-21] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-33] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-60] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-68] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-76] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-37] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-48] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-150] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-120] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-164] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-174] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-181] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.