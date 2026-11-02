# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_64`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 130: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [118–132], lower_priority='Action_ZoneBlock' annotated_start=124, effective_Action_ZoneBlock_start=133.
> - Action 'Action_BallCarry' range [150-225] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-234] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-168] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-178] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-260] for track '3' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [263-264] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-153] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-269] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-184] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-130] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [135-143] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-157] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [147-152] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-231] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [237-245] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-257] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-33] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-89] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-134] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-265] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-258] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-202] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-246] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-269] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '28' has 2 frames without a visible bounding box.
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
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.