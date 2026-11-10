# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_71`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_71/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [49-299] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-233] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-292] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-202] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-111] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-68] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [86-87] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-204] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-198] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-216] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-247] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-225] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-159] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-66] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-175] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [49-127] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-197] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [59-92] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-172] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-182] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-215] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-173] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-177] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [50-65] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [71-130] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [92-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-127] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-149] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-150] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-158] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-194] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-182] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-194] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-274] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-288] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [286-288] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '36' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.