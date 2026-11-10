# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_49`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_49/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 119 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_None' range [103-156] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-192] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-148] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-158] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [162-191] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-242] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-196] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [103-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-215] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-166] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-294] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-309] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-304] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-316] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-325] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [121-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-226] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-154] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-217] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-329] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-152] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [156-203] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-155] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-304] for track '13' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [103-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-140] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-152] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-226] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [108-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-111] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-141] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [156-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-195] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [104-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-138] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [140-149] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-170] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-193] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-166] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-227] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-168] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-213] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [180-189] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-202] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [191-219] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-243] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-233] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-247] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-229] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-240] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-302] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-309] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-313] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [274-276] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-289] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [302-329] for track '36' has 1 frames without a visible bounding box.
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