# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_329`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_329/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 47 |
| Player Tracks | 47 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [28–41], lower_priority='Action_ZoneBlock' annotated_start=31, effective_Action_ZoneBlock_start=42.
> - Action 'Action_None' range [28-124] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-236] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-64] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-105] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [28-76] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-85] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-111] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-220] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-127] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-213] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [55-71] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [72-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [28-137] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-91] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-97] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-92] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-105] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-211] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-153] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-205] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-162] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-158] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-227] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-186] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [199-201] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-211] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-214] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-222] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-229] for track '34' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [220-227] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-239] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-238] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-237] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-238] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '46' has 1 frames without a visible bounding box.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.