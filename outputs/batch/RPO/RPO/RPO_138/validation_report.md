# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_138`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_138/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_ZoneBlock' range [65-90] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-105] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-116] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [64-171] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-233] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-165] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-163] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-188] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [209-229] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-170] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-128] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-192] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-174] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-183] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-119] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-130] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-167] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-96] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-157] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-128] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-128] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-182] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [122-198] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-222] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-170] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-146] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-152] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-162] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-157] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-197] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-239] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-238] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-233] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-227] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '32' has 1 frames without a visible bounding box.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.