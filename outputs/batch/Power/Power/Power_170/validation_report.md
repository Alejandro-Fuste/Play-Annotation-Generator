# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_170`
- **Input XML**: `outputs/batch/Power/Power/Power_170/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 342: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 342: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Action 'Action_PreSnap' range [9-183] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [236-273] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [278-280] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [293-303] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-313] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [329-419] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [236-253] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-267] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-291] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [302-315] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [319-328] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [333-419] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-289] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-66] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-372] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-376] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-292] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-325] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-414] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-256] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-277] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-353] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-365] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [236-250] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [253-307] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-240] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-75] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-242] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-307] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [315-316] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [326-327] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-65] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-90] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-293] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-234] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-275] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-328] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-276] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-304] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-321] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-326] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-382] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-325] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-419] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [340-353] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-356] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-419] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-376] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-412] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [406-408] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [414-417] for track '26' has 2 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.