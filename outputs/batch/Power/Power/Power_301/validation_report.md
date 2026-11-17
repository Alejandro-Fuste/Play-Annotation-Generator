# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_301`
- **Input XML**: `outputs/batch/Power/Power/Power_301/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 92 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 569 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 602: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Track ID '22' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 569 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '5' (DE2) duration 94 frames exceeds threshold 90 frames [start=346, end=439].
> - Validation warning: Action 'Action_DownBlock' for track '18' (C) duration 94 frames exceeds threshold 90 frames [start=346, end=439].
> - Validation warning: Action 'Action_DownBlock' for track '21' (Unknown) duration 94 frames exceeds threshold 90 frames [start=346, end=439].
> - Validation warning: Action 'Action_DownBlock' for track '22' (RG) duration 94 frames exceeds threshold 90 frames [start=346, end=439].
> - Action 'Action_PreSnap' range [13-504] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-490] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [492-569] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-191] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-526] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [528-569] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-531] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [540-558] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-509] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [529-541] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-476] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [482-487] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [489-507] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [509-569] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-436] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [438-439] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [446-449] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-420] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [425-516] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [520-531] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-472] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-32] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-521] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-425] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [428-432] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [435-436] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-448] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [346-406] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [413-414] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [417-439] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [440-455] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-17] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-27] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-66] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-436] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [448-450] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [454-457] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [463-465] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [471-472] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [474-544] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-345] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [346-400] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [452-455] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [346-402] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-194] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-207] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [210-211] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [248-249] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [408-409] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [418-420] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [439-449] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [454-455] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [457-463] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [465-481] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [498-500] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [452-569] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [453-454] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [468-470] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [472-478] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [481-482] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [484-569] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [500-504] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [508-527] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [531-532] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [507-533] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [537-543] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [546-562] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [527-532] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [542-543] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [549-554] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [561-564] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [529-558] for track '34' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.