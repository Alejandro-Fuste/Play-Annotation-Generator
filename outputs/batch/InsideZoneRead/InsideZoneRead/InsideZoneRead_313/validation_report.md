# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_313`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_313/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 130 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '5' has invalid range: start=8, end=4. Clamping end to start.
> - Action 'Action_None' range [5-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-63] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-89] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-128] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-161] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-32] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [35-36] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-53] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-57] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-180] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [59-91] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [97-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-89] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-100] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-126] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-155] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [163-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-51] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-58] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-165] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-131] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-58] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-180] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [5-39] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-60] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-73] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [81-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-180] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-49] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [52-61] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-76] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [85-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-180] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-180] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [41-48] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [53-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [69-96] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-135] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-180] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [8-28] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-27] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-54] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-61] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-71] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-20] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-35] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-64] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-104] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-33] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-59] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-85] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-155] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-36] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-71] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-89] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [93-100] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-113] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-180] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-180] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-87] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-101] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-108] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-118] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-180] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-157] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [159-170] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-136] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-151] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-173] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-180] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-180] for track '35' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [141-180] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-157] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-180] for track '38' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_313'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.