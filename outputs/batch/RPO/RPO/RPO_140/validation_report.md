# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_140`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_140/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_ZoneBlock' range [31-67] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-150] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-115] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-105] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-134] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-107] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-116] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-144] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-29] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-137] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-62] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-90] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-96] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [98-99] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-110] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [30-102] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-122] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-55] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-43] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-82] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [31-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-50] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-83] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [54-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-84] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-93] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-121] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [127-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-94] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-158] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-98] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-183] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-134] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-149] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-137] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-153] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-159] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-160] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.