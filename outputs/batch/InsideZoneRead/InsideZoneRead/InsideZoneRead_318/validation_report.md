# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_318`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_318/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '2' has invalid range: start=76, end=64. Clamping end to start.
> - Segment 'Action_ZoneBlock' for track '14' has invalid range: start=76, end=72. Clamping end to start.
> - Segment 'Action_ReadDefender' for track '14' has invalid range: start=95, end=76. Clamping end to start.
> - Segment 'Action_Keep' for track '14' has invalid range: start=102, end=76. Clamping end to start.
> - Segment 'Action_BallCarry' for track '14' has invalid range: start=122, end=76. Clamping end to start.
> - Segment 'Action_BlockSecondLevel' for track '15' has invalid range: start=107, end=26. Clamping end to start.
> - Action 'Action_PreSnap' range [0-57] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-12] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-77] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-64] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-65] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-67] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [76-89] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-191] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '5' starts at frame 73, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [73-73] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-27] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-47] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-116] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [73-93] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-116] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-141] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-147] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-2] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-13] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-37] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-59] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-106] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [73-76] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-26] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-44] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-33] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-99] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-62] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-190] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-55] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-67] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-87] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-85] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-125] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-135] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-200] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-163] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-148] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-161] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-167] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-181] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-210] for track '30' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_318'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.