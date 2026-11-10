# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_209`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_209/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Overlapping action conflict at frame 67 for track '20': 'Action_ReadDefender' vs 'Action_PullBall'. Overriding with 'Action_PullBall'.
> - Action 'Action_None' range [48-227] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-234] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-263] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-143] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-149] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-232] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-269] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-144] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-161] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-240] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-237] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-257] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-141] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [145-168] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [48-269] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [48-79] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-130] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-269] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [104-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-269] for track '16' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-143] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-147] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-178] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-183] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [49-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-84] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-126] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-144] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-184] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-192] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-258] for track '35' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.