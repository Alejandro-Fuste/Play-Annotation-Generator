# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutRoutes_123`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_123/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 152 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 130: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_BallCarry' range [137-228] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [250-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-96] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-101] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-145] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-156] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-236] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-67] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-90] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-145] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-188] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [173-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-235] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-77] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-96] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-186] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-203] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [254-256] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-266] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-42] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-47] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [55-56] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-84] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-218] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [233-240] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [74-75] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-95] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-47] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-76] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-89] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-109] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-247] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-257] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-262] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-86] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ThrowPass' range [87-94] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-47] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-47] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [106-115] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [139-147] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [158-160] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [167-231] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [234-237] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [239-240] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [243-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-102] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-125] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-203] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-108] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-116] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-121] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-224] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-232] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-236] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [238-240] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-118] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-122] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-131] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-158] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-175] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-181] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-196] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-222] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-269] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-132] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-182] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-187] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-200] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [216-217] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-231] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [235-237] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-269] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-151] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [158-159] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-220] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-141] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-269] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-152] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-166] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [170-182] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [184-232] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [234-236] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-267] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [171-174] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-226] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-238] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-255] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-256] for track '42' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.