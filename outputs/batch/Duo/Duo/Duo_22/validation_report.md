# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_22`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '4' has invalid range: start=248, end=245. Clamping end to start.
> - Action 'Action_PreSnap' range [0-245] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [223-270] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [275-289] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-275] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-326] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [223-237] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [239-240] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [244-245] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-322] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-275] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-293] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-222] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [223-289] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '10' starts at frame 290, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [290-290] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-308] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-220] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-328] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-291] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-145] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-191] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-194] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-296] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [314-326] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-80] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [65-68] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-108] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-157] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-177] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [223-268] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [275-285] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-304] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [311-312] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-121] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [287-290] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-290] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-311] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-275] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-307] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-291] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-322] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [292-295] for track '26' has 1 frames without a visible bounding box.
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