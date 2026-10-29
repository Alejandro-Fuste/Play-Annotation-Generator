# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_95`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_95/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 132 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 418 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 192: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 418 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '7' (RT) duration 116 frames exceeds threshold 90 frames [start=219, end=334].
> - Validation warning: Action 'Action_BlockSecondLevel' for track '19' (C) duration 116 frames exceeds threshold 90 frames [start=219, end=334].
> - Action 'Action_PreSnap' range [0-300] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-409] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-308] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-141] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-161] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-169] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-181] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-280] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-340] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [343-418] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [18-240] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-372] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-376] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-380] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-381] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-73] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-141] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [219-233] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [236-237] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [248-251] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [254-283] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [286-288] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [292-333] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-359] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-410] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-402] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-295] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-331] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-410] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-45] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [48-49] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-73] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-121] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-129] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-153] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-237] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-259] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-295] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-392] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [394-405] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-129] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-161] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-259] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-295] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-73] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-77] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-129] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-169] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-185] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-240] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-290] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [18-77] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [79-81] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [83-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [110-129] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [132-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [144-165] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [184-185] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [208-240] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [244-259] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [261-330] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-347] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [47-86] for track '18' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-141] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-161] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-247] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [250-357] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [18-193] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [219-334] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [335-388] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [402-418] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-121] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-369] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-81] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-161] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [246-259] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-325] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-359] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-418] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [354-358] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [358-403] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-407] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-391] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-407] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [409-418] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-418] for track '26' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.