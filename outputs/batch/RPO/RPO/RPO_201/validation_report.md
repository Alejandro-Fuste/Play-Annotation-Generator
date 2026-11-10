# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_201`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_201/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [44-53] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-189] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-204] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-132] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-163] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-43] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '9' starts at frame 44, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [44-44] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [47-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-97] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-112] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-148] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-199] for track '11' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [201-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-55] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-105] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-121] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-49] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [45-49] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-72] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-51] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-55] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-70] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-82] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-122] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-142] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-94] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-156] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-173] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [189-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-126] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-182] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-194] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-169] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-150] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-188] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-152] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-176] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-209] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '39' has 1 frames without a visible bounding box.
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