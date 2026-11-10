# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_185`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_185/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 99 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [47-239] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-183] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-193] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-214] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-222] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-177] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-209] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-221] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-238] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-226] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-198] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [207-216] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-155] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-194] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-107] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-165] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-212] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-93] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [106-118] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-123] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-190] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [197-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-170] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [58-72] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-76] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-123] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-190] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-212] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [48-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-86] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-224] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-212] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-228] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.