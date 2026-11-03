# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_69`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_69/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 46 |
| Player Tracks | 46 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 125 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_BallCarry' range [125-169] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [173-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-236] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-67] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-84] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-101] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-188] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-243] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-250] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-419] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-418] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-89] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-243] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-247] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-419] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-302] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [304-305] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [308-419] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-163] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-351] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [364-374] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-383] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-300] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-314] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [321-322] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-103] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-39] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-91] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-143] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [84-256] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-74] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [76-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-87] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [96-206] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [209-215] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [218-225] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [227-307] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-237] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-214] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [52-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [78-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-91] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-257] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [259-298] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-233] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-66] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-419] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-84] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-256] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-270] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-188] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-232] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-274] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [279-280] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-225] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-283] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-377] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-419] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [218-222] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-229] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-245] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-235] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-272] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-250] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-281] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-381] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-394] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-275] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-315] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-419] for track '35' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-266] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-276] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-419] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-316] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-311] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-366] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [371-386] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [389-391] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-380] for track '43' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [392-394] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-411] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-418] for track '44' has 2 frames without a visible bounding box.
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
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.