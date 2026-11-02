# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_81`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_81/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 108 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [34–45], lower_priority='Action_ZoneBlock' annotated_start=39, effective_Action_ZoneBlock_start=46.
> - Action 'Action_SealBlock' range [39-157] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [159-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [46-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-226] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-132] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-130] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-226] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-72] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-121] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-212] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-233] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-170] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [34-41] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [60-224] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-57] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-81] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-143] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-126] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-138] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-158] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-226] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-201] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-217] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-205] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-207] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [210-215] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-215] for track '36' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [217-222] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-236] for track '37' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.