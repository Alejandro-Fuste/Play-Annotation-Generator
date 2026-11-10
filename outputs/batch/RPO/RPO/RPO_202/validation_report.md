# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_202`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_202/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [60-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-105] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-153] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-199] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-206] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-193] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-169] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-62] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [70-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [89-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [100-128] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-206] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-111] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-176] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-210] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [61-64] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-117] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '16' starts at frame 61, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [61-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-165] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-19] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-53] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-65] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-54] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-62] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-110] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-93] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-101] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-111] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-135] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-105] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-160] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-107] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-210] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-204] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '27' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.