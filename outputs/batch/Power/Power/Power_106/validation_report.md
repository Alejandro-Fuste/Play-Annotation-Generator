# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_106`
- **Input XML**: `outputs/batch/Power/Power/Power_106/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 40 |
| Ball Tracks | 0 |
| CSV events parsed | 11 |
| Action Segments inferred | 88 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Overlapping action conflict at frame 150 for track '4': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
> - Action 'Action_PreSnap' range [24-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-176] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [179-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-240] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [244-257] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-265] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [150-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [169-176] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-158] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-224] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-226] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-275] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-102] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-122] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-157] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-180] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-216] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-248] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-167] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-51] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-184] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-237] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-243] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-252] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-274] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-283] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-189] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [161-162] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-154] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-196] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-329] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-55] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-75] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-102] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-110] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-153] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-174] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-329] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-205] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [189-221] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-256] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-265] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-277] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-324] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [327-328] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-231] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-297] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [299-329] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [215-239] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [222-225] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [228-232] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-243] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [245-280] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [282-286] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [289-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-247] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-253] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [256-329] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-289] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-329] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-280] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-327] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-299] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-308] for track '36' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.