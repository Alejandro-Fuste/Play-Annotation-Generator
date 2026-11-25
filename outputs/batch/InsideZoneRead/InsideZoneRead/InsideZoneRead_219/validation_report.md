# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_219`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_219/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 34 |
| Ball Tracks | 1 |
| CSV events parsed | 21 |
| Action Segments inferred | 79 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BlockSecondLevel' for track '17' has invalid range: start=141, end=110. Clamping end to start.
> - Action 'Action_None' range [109-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-231] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-192] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-156] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [166-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [190-197] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-148] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-127] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-146] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-172] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [151-193] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-161] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-6] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-34] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-38] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-121] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-233] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-14] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [112-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-158] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 198, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [198-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-110] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-64] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-161] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-162] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-239] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-178] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-224] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-213] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-217] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-219] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '34' has 1 frames without a visible bounding box.
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
> - Metadata: no Dataset Summary row found for output_file 'InsideZoneRead_219'; source metadata written as null.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.