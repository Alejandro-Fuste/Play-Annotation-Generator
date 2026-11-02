# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_174`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_174/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 76 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 350: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Track ID '21' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [141–147], lower_priority='Action_ZoneBlock' annotated_start=143, effective_Action_ZoneBlock_start=148.
> - Action 'Action_None' range [197-203] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-222] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-193] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-297] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-257] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [143-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-207] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-215] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-99] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-111] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-299] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-256] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-231] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-18] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-279] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-285] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [169-272] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-162] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-299] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-217] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-267] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-299] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-270] for track '23' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [272-279] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-222] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-278] for track '26' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [279-299] for track '28' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.