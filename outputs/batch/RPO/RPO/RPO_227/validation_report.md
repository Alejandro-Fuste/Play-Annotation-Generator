# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_227`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_227/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
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
> - Segment 'Action_PullBall' for track '25' has invalid range: start=108, end=69. Clamping end to start.
> - Action 'Action_None' range [22-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-60] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-79] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-111] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-169] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-161] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-173] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-193] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [22-33] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [31-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [102-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-60] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-79] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-111] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-210] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-43] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-210] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [23-35] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-87] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-96] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-206] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [27-28] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-173] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-194] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-144] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-160] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-208] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-198] for track '30' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '33' has 1 frames without a visible bounding box.
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