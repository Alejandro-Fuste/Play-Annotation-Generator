# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_350`
- **Input XML**: `outputs/batch/Power/Power/Power_350/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 10 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '15' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Action 'Action_PreSnap' range [19-234] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-270] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [272-281] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-338] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [342-449] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-292] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-335] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-346] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [232-242] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-368] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-306] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-319] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-327] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-332] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [232-262] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-360] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-323] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-347] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [353-365] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-401] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-426] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [430-431] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-266] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [268-350] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-90] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-231] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-235] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [251-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [257-259] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-449] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-231] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [232-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [242-243] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [246-261] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [278-281] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [283-292] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-434] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [438-441] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-116] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-405] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-226] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [253-284] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-276] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-378] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [285-422] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-371] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-411] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-421] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-378] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [381-397] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [405-406] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-336] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-388] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [390-449] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-352] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-373] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [378-379] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-388] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [391-410] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-365] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-371] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-391] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [341-353] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-358] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-371] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-374] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [347-362] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-381] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [383-417] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [426-446] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-374] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [385-393] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-439] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [444-447] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-400] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [402-403] for track '28' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.