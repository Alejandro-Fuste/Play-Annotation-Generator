# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_54`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 78 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [47-124] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-114] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-180] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-148] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-70] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [71-76] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [99-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [51-75] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-61] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-124] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-69] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-94] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-69] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-161] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-64] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-100] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-118] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-137] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-154] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-169] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-155] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-180] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-180] for track '24' has 2 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.