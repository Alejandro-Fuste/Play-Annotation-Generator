# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_44`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_44/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 298 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 298 as fallback play end.
> - Action 'Action_PreSnap' range [0-241] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-278] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-287] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-298] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-205] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-246] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-264] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-274] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-287] for track '4' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [154-212] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-253] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-187] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-260] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [154-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-267] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-225] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-298] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-98] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-179] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-192] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-201] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [203-206] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-214] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-226] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-235] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-240] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-296] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-272] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-240] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-273] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-83] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-241] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-298] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-65] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-84] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-143] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-252] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-263] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-282] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-254] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-123] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-129] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [154-186] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-269] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [273-295] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-215] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-298] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-208] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-266] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-230] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-263] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [232-257] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-236] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-240] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-298] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-251] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-259] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-271] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [269-271] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-293] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-296] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [288-294] for track '35' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.