# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_283`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_283/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [60-279] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-154] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-222] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-293] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-291] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [63-116] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-299] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-134] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-151] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-164] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-291] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [106-293] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_Handoff' range [90-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-87] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-146] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-145] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-157] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-195] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-290] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-84] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-93] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-138] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-62] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-39] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [63-93] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [115-119] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-97] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-163] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-183] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-266] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [166-201] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-299] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-196] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-246] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [248-291] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-293] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-256] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-293] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-268] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [274-275] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-287] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-297] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-296] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-299] for track '40' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.