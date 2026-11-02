# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_66`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_66/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 133: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [72–84], lower_priority='Action_ZoneBlock' annotated_start=73, effective_Action_ZoneBlock_start=85.
> - Action 'Action_None' range [72-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [31-70] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [101-269] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-185] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-128] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-262] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-264] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-142] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-158] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-252] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-258] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-181] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [72-83] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-90] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-177] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-258] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-213] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-267] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-244] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [246-255] for track '27' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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