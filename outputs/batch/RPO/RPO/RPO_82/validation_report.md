# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_82`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_82/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_ZoneBlock' range [74-85] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-158] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-173] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-152] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-170] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-187] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-129] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-85] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [87-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-187] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-156] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [73-168] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-167] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PullBall' range [91-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-131] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' for track '10' starts at frame 135, but the player has no visible bounding box on this frame.
> - Action 'Action_ThrowPass' range [135-135] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-156] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-111] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-139] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-166] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-4] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-61] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-84] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-151] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-156] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-124] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-164] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-191] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [179-182] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-234] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-229] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-249] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-257] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-290] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-257] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-229] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-261] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-267] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-283] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-304] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-270] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-283] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-270] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-273] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-284] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-290] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [305-306] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-290] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-297] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-338] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-343] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-352] for track '38' has 1 frames without a visible bounding box.
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