# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_55`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [41-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-74] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [77-125] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [41-176] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-107] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-152] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-176] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-102] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-128] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-180] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-73] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-95] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-86] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 87, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [87-87] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-166] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-104] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-132] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [41-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-178] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '21' starts at frame 42, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [42-42] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-50] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-88] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-165] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-180] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-104] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-125] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-174] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-180] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-129] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-150] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-180] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-161] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-151] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-176] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-164] for track '38' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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