# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_80`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_80/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 162: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [52–61], lower_priority='Action_ZoneBlock' annotated_start=55, effective_Action_ZoneBlock_start=62.
> - Action 'Action_BallCarry' range [76-204] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [211-232] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [242-246] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [248-251] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-260] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [52-77] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-112] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-182] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-222] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-246] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-225] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [52-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-125] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-269] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-82] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-17] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-269] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-230] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '25' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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