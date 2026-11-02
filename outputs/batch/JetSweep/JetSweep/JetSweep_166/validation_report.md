# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_166`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_166/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Overlapping action conflict at frame 93 for track '2': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [92–106], lower_priority='Action_ZoneBlock' annotated_start=93, effective_Action_ZoneBlock_start=107.
> - Action 'Action_None' range [92-155] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-228] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-137] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-162] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-123] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-140] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-222] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-165] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-8] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-106] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [92-115] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [121-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [127-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-158] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-182] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [187-225] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-293] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [93-161] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-191] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-155] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-162] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-205] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-243] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-292] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-297] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-250] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-279] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [272-276] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [283-299] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '38' has 1 frames without a visible bounding box.
> - Player track '5' has undefined position. Will map to Position_Unknown.
> - Player track '5' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.