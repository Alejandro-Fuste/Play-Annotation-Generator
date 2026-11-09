# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_3`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 90 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [0-64] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-84] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-97] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [101-185] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-145] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-119] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-82] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-127] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-171] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-76] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '8' starts at frame 77, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [77-199] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [61-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [33-76] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-153] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-163] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-205] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-103] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-54] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-58] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-51] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-58] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-114] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-149] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-110] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-119] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-133] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-212] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-106] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-115] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-122] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-110] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-175] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-129] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-163] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [199-200] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-237] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-246] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-305] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-263] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-271] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [266-292] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [267-269] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [324-327] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.