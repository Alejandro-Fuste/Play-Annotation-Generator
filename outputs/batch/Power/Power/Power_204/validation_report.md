# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_204`
- **Input XML**: `outputs/batch/Power/Power/Power_204/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 52 |
| Player Tracks | 52 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 147 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 410: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 410: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Action 'Action_PreSnap' range [4-374] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [380-381] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-173] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-292] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-386] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-169] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-323] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [382-392] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-452] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-417] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-318] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-146] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [181-182] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [187-192] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [194-198] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-223] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-280] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [286-320] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [329-447] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-173] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-267] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-156] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-133] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-159] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [164-316] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-509] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-79] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-125] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-316] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-10] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-141] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-168] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-17] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-390] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-251] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-42] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-125] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-106] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-151] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-183] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-194] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [196-211] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [213-281] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [283-366] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [377-455] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-469] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [472-482] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [484-488] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [491-494] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-139] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-161] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-176] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-234] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-248] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-259] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-278] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-149] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [204-205] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [298-308] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [320-346] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [351-354] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-356] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-362] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-402] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-232] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-240] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-321] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-334] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [338-341] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-376] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [379-380] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-221] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-224] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [274-277] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [298-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [323-325] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [330-335] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [337-354] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [355-369] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-373] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-378] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-317] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [291-295] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [320-321] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [325-391] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [396-398] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [400-404] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [298-323] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [325-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-351] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-521] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [336-342] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [344-398] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [339-347] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [355-452] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-473] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-404] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-453] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-479] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [372-417] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [430-434] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [437-454] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [374-379] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [375-395] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [397-398] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [401-402] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [404-406] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [386-433] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [452-457] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [398-399] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-411] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [412-569] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [415-417] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-495] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [450-453] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [464-477] for track '46' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [489-569] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [528-569] for track '49' has 3 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.
> - Player track '51' has undefined position. Will map to Position_Unknown.
> - Player track '51' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.