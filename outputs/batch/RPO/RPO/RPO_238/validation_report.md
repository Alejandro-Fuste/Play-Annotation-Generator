# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_238`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_238/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 31 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 84 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [55-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-138] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-128] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-133] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-131] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-125] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-146] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-99] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-130] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-125] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-87] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-96] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-133] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-77] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-125] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 55, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [55-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [67-71] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-65] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-80] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-142] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-124] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-110] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-144] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [114-132] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-145] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-165] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-169] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-195] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-206] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-191] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '31' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.