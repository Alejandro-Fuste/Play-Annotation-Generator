# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Dagger_30`
- **Input XML**: `outputs/batch/Dagger/Dagger/Dagger_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Dagger.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [148–154], lower_priority='Action_PassBlock' annotated_start=151, effective_Action_PassBlock_start=155.
> - Action 'Action_None' range [255-314] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-324] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-300] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-309] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-253] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [148-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-303] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [151-222] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [226-238] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-307] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [155-221] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [224-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-211] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-308] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-252] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-329] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [255-265] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-324] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-329] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.