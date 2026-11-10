# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_89`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_89/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [29-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-72] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-83] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-88] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-238] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-39] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [30-61] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-185] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-72] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-116] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-105] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-73] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-216] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-194] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-50] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-197] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-56] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-20] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-28] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 29, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [29-33] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [76-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-156] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-184] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [39-73] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-58] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-70] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-86] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-109] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-269] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-233] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-251] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-262] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-122] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-160] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-147] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-234] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-246] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [251-258] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-193] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-269] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-269] for track '29' has 2 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.