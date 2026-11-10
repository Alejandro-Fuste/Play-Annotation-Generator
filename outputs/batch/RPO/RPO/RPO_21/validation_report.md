# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_21`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [53-115] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-121] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-218] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-218] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [72-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-243] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-63] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-115] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-235] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-265] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-250] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-265] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-105] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-264] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-259] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-192] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-168] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-224] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-239] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-233] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [239-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-224] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-255] for track '33' has 1 frames without a visible bounding box.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.