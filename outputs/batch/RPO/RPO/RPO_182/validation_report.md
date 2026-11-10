# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_182`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_182/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [41-74] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-119] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-129] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [142-146] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-235] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-74] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-95] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-152] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-128] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-88] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-261] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [42-56] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-40] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-44] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-58] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-64] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-247] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-149] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-132] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-253] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-163] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-202] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-160] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.