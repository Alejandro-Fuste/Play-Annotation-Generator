# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `BootPass_68`
- **Input XML**: `outputs/batch/BootPass/BootPass/BootPass_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/BootPass.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 53 |
| Player Tracks | 53 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 130 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 419 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 419 as fallback play end.
> - Segment 'Action_BootAway' for track '15' has invalid range: start=78, end=65. Clamping end to start.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [34–40], lower_priority='Action_RunBlock' annotated_start=5, effective_Action_RunBlock_start=41.
> - Action 'Action_None' range [34-102] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-133] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-294] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-377] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-385] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-76] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [5-33] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [46-51] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [58-66] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [73-78] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [103-187] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [34-108] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-94] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-105] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-172] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [5-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [71-99] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [117-122] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [140-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-20] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-82] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-117] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [5-51] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [69-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [128-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [177-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [222-261] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [264-268] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [271-279] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [281-283] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunBlock' range [289-290] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-62] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-125] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-45] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-243] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-334] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [34-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [50-59] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_FakeHandoff' range [64-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-55] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-107] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [114-192] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-31] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [37-48] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-33] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-37] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-51] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [42-61] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [55-92] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-108] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-99] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-123] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-117] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-130] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-140] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-127] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-118] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-123] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-138] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-162] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-202] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-256] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-273] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-148] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-286] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-300] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-153] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-200] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-409] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-167] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-419] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-192] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-323] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [333-338] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [284-294] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-298] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-315] for track '44' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-325] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-328] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [390-395] for track '50' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [396-399] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [402-404] for track '51' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [406-419] for track '51' has 2 frames without a visible bounding box.
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
> - Player track '52' has undefined position. Will map to Position_Unknown.
> - Player track '52' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.