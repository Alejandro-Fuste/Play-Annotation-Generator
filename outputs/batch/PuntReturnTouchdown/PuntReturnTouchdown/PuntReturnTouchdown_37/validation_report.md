# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntReturnTouchdown_37`
- **Input XML**: `outputs/batch/PuntReturnTouchdown/PuntReturnTouchdown/PuntReturnTouchdown_37/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntReturnTouchdown.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 40 |
| Ball Tracks | 1 |
| CSV events parsed | 13 |
| Action Segments inferred | 147 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 599 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 76: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - Row 76: Duplicate assignment for track ID '16' in grid. Overwriting previous assignment.
> - Row 76: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 599 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [26-533] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [535-545] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-549] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-192] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-442] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-50] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-176] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-198] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-342] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [345-569] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [26-340] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [351-490] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-152] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-337] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-169] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [98-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-40] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-311] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-455] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [460-465] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [467-468] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [473-506] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [509-510] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [513-548] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [552-580] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-571] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-58] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-165] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-453] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [455-460] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-182] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-199] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-405] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [409-416] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [418-433] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-440] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [445-449] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [474-476] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [482-487] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [491-492] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [497-500] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-82] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-137] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-165] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [26-103] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-54] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-234] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-242] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-246] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-316] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-342] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [344-599] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-77] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-345] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-381] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [386-513] for track '20' has 8 frames without a visible bounding box.
> - Action 'Action_None' range [517-530] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [533-535] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-125] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-139] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-271] for track '21' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [273-348] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [353-524] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-158] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [285-453] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [455-587] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-295] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [299-462] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [464-583] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-544] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [547-593] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-334] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [337-453] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [266-409] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [411-433] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [437-442] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [444-457] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [461-468] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [283-285] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-599] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [306-556] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-504] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [369-431] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [435-436] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [441-482] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [484-528] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [441-445] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [448-449] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [521-523] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [525-527] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [529-532] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [527-530] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [533-599] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [556-560] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [562-563] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [569-599] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [590-592] for track '40' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_SpecialTeams_PuntReturnTouchdown'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.