# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_303`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_303/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [18–26], lower_priority='Action_ZoneBlock' annotated_start=21, effective_Action_ZoneBlock_start=27.
> - Action 'Action_None' range [18-198] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-191] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-31] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-81] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-143] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-187] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-110] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-231] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [42-43] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [45-49] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-93] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-38] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-144] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-148] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [49-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [80-155] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-205] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [212-231] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-41] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-62] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-32] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [35-36] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [59-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-151] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-32] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-133] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-136] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-187] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [18-26] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-43] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-68] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-109] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [21-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [58-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [66-83] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-93] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-109] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-219] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-165] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-228] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-239] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-239] for track '30' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.