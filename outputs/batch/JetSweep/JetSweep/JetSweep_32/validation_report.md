# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_32`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_32/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [122–135], lower_priority='Action_ZoneBlock' annotated_start=126, effective_Action_ZoneBlock_start=136.
> - Action 'Action_None' range [122-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-183] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [126-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-186] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-161] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-187] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-192] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-191] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-191] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-181] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-188] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-121] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-137] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-80] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-152] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-142] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-133] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [128-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [153-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [186-299] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [306-307] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [310-315] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-191] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-329] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-235] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-273] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-329] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [191-232] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-267] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-236] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-207] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-248] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-255] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-314] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-329] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-319] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [287-306] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-315] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-327] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-329] for track '38' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.