# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_221`
- **Input XML**: `outputs/batch/Power/Power/Power_221/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 103 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 689 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 444: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 689 as fallback play end.
> - Action 'Action_PreSnap' range [0-625] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [627-642] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [648-662] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-689] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-605] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-537] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-627] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [629-649] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [653-670] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-605] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [607-608] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [611-612] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [618-622] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [640-643] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [645-689] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-689] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-378] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [445-637] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [649-651] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [653-658] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [660-676] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-609] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [611-623] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [635-636] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [639-642] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [652-653] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-628] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [632-666] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [669-672] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-526] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [530-532] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [537-622] for track '11' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [624-656] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-634] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [636-679] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-323] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-368] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [373-396] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-543] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [546-547] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [553-689] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-519] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [521-568] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [574-640] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [648-689] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [514-533] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-534] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [536-689] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [555-637] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [639-640] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-607] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [609-673] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-637] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [644-645] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [647-654] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-371] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [376-377] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [514-521] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [531-554] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [555-623] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [626-687] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [78-81] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-89] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-108] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-113] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-386] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [555-616] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [619-622] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [632-633] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [539-540] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [542-689] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [565-566] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [592-595] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [619-652] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [655-658] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [661-673] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [679-680] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [652-674] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [676-681] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [684-687] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [664-665] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [685-686] for track '33' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.