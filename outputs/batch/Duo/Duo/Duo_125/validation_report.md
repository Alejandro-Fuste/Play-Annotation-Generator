# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_125`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_125/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 268 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 268 as fallback play end.
> - Segment 'Action_ComboBlock' for track '27' has invalid range: start=207, end=158. Clamping end to start.
> - Action 'Action_PreSnap' range [0-195] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-214] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-234] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [195-268] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-155] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-268] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-197] for track '7' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-221] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-221] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-229] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-234] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [121-147] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [152-154] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-172] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-238] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-220] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-240] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-185] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-188] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-167] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [168-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [208-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-268] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-165] for track '21' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-133] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-154] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-182] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-268] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-250] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-201] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-231] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-216] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-219] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-268] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-261] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.