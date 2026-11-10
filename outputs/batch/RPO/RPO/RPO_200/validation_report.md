# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_200`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_200/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 40 |
| Ball Tracks | 1 |
| CSV events parsed | 16 |
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
> - Action 'Action_None' range [33-213] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-201] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-116] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-49] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [51-87] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [91-94] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-143] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-66] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-190] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-189] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-199] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-98] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [103-194] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-148] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '8' has 5 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-84] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-175] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [33-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-63] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [65-66] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [74-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-165] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-172] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-106] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-194] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-106] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-148] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [151-165] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-164] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-176] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-192] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-204] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-187] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-175] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-189] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-206] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-229] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-228] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-232] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-228] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-233] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-239] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-232] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '40' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.